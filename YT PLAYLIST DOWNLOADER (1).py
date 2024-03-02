#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install pytube


# In[1]:


from pytube import YouTube


# In[2]:


dir(YouTube)


# In[3]:


link = "https://youtube.com/playlist?list=PLgUwDviBIf0


# In[4]:


try:
    yt = YouTube(link)
    print(yt)
    pass
except Exception as error:
    print(f"Error: {error}")
    pass


# In[10]:


print(yt.streams)


# In[11]:


yt.title


# In[5]:


from pytube import Playlist


# In[37]:





# In[38]:





# In[42]:





# In[48]:





# In[60]:





# In[66]:


playlist_url = "https://youtube.com/playlist?list=PLgUwcIDCZnxhv0LkHf5KzyqM"


# In[54]:





# In[67]:


p = Playlist(playlist_url)


# In[ ]:





# In[1]:


print(f'Youtube playlist title is : {p.title} ')


# In[69]:


for url in p.video_urls:
    print(url)


# In[70]:


save_video_path = '/Users/username/Desktop/yt_videos/tries'


# In[71]:


for video in p.videos:
    try:
        stream = video.streams.get_by_itag(22)
        stream.download(output_path = save_video_path)
    except Exception as error:
        print(f"Error while downloading the video: {error}")
        pass
    pass

print(f"YouTube videos downloaded successfully at {save_video_path}.")


# In[ ]:




