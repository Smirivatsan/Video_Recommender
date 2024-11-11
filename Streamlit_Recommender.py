import streamlit as st
import json
import requests
import pandas as pd
import numpy as np

def read_json(filename,encoding):
    with open(filename, 'r', encoding=encoding) as file:
        try:
            data = json.load(file)  # json.load() reads and decodes JSON from a file
            return data
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
            
# Tag database
tag_db = read_json("tags_utf8.json","utf-8")

# Function to find the best advertisement based on tags
def find_correlation(test_video, ads):
    for ad in ads:
        for videotag in test_video['tags']:
            if videotag in ad['tags']:
                st.write(f"Recommended advertisement: {ad['title']}")
                return ad['url']
    return None

# Main Streamlit application
st.title("Video and Recommended Advertisement")

# Get video URL and tags from the user
video_url = st.text_input("Enter the video URL")
video_tags = st.text_input("Enter video tags (comma-separated)")

# Button to recommend advertisement
if st.button("Find Recommended Advertisement"):
    if video_url and video_tags:
        # Process video tags and find a matching ad
        test_video = {"url": video_url, "tags": video_tags.split(",")}
        recommended_ad_url = find_correlation(test_video, sample_ads)
        
        # Display the input video
        st.subheader("Your Video:")
        st.video(video_url)

        # Display the recommended ad if found
        if recommended_ad_url:
            st.subheader("Recommended Advertisement:")
            st.video(recommended_ad_url)
        else:
            st.write("No suitable advertisement found.")
    else:
        st.write("Please enter both the video URL and tags.")