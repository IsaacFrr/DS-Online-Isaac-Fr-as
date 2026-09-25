"""Herramientas reproducibles para los ejercicios de Gymnasium y Taxi."""
from pathlib import Path
import numpy as np
import pandas as pd
import gymnasium as gym
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

SEED=42
TAXI_ID='Taxi-v4' if 'Taxi-v4' in gym.registry else 'Taxi-v3'

def animate(frames,interval=70):
    if not frames:raise ValueError('No hay fotogramas')
    fig,ax=plt.subplots(figsize=(5,4));ax.axis('off')
    image=ax.imshow(frames[0])
    def update(i):image.set_data(frames[i]);return (image,)
    animation=FuncAnimation(fig,update,frames=len(frames),interval=interval)
    html=HTML(animation.to_jshtml());plt.close(fig);return html

def episode(policy,seed=42,render=False):
    env=gym.make(TAXI_ID,render_mode='rgb_array' if render else None)
    state,info=env.reset(seed=seed);rng=np.random.default_rng(seed)
    rewards=[];penalties=0;frames=[];success=False
    if render:frames.append(env.render())
    for step in range(200):
        if isinstance(policy,np.ndarray):action=int(np.argmax(policy[state]))
        elif policy=='masked':action=int(rng.choice(np.flatnonzero(info['action_mask'])))
        else:action=int(rng.integers(env.action_space.n))
        state,reward,terminated,truncated,info=env.step(action)
        rewards.append(reward);penalties+=int(reward==-10)
        if render:frames.append(env.render())
        if terminated or truncated:
            success=bool(terminated);break
    env.close()
    return dict(pasos=len(rewards),penalizaciones=penalties,recompensa=sum(rewards),exito=success),frames

def evaluate(policy,episodes=100,start_seed=200000):
    rows=[episode(policy,start_seed+i)[0] for i in range(episodes)]
    data=pd.DataFrame(rows)
    return pd.Series({'pasos/episodio':data.pasos.mean(),'penalizaciones/episodio':data.penalizaciones.mean(),
        'recompensa/acción':data.recompensa.sum()/data.pasos.sum(),'éxito':data.exito.mean()})

def train_taxi(episodes=100000,alpha=.05,gamma=.9,epsilon=.1,seed=42):
    env=gym.make(TAXI_ID);rng=np.random.default_rng(seed)
    q=np.zeros((env.observation_space.n,env.action_space.n));rows=[]
    for i in range(episodes):
        state,info=env.reset(seed=seed+i);penalties=0;total=0
        for step in range(200):
            if rng.random()<epsilon:action=int(rng.integers(env.action_space.n))
            else:action=int(rng.choice(np.flatnonzero(q[state]==q[state].max())))
            new,reward,terminated,truncated,info=env.step(action)
            # El estado terminal no tiene valor futuro. La truncación limita el episodio.
            target=reward+(0 if terminated else gamma*q[new].max())
            q[state,action]+=alpha*(target-q[state,action])
            state=new;total+=reward;penalties+=int(reward==-10)
            if terminated or truncated:break
        rows.append((step+1,penalties,total))
    env.close()
    assert np.isfinite(q).all()
    return q,pd.DataFrame(rows,columns=['pasos','penalizaciones','recompensa'])

def cache_path():
    root=next(p for p in Path.cwd().parents if (p/'.git').exists())
    folder=root/'.cache'/'unidades_siguientes';folder.mkdir(parents=True,exist_ok=True)
    return folder/f'q_taxi_{TAXI_ID}_100000_seed42.npz'

def load_or_train():
    path=cache_path()
    if path.exists():
        with np.load(path) as data:q=data['q'].copy()
    else:
        q,history=train_taxi();np.savez_compressed(path,q=q)
    assert q.shape==(500,6) and np.isfinite(q).all()
    return q
