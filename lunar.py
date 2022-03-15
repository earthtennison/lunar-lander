import gym 
import random

env = gym.make("LunarLander-v2")
episodes = 3
for episode in range(1,episodes+1):
    state = env.reset()
    done =False
    score = 0 

    while not done:
        env.render()
        action = env.action_space.sample()
        print(action)
        n_state, reward, done, info =env.step(action)
        print("n_state: {} reward: {} done: {} info: {} ".format(n_state, reward, done, info))
        score += reward
    print('Episode: {} Score: {}'.format(episode, score))
env.close

# def main():
#     env = gym.make('')
#     env.reset()
#     ret = env.step(0)
#     print(ret)

# if __name__ == "__main__":
#     main()
