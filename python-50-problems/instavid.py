import instaloader

# Create an instance of Instaloader
L = instaloader.Instaloader()

# Enter the shortcode of the post/reel (found in the URL)
# Example URL: https://instagram.com -> shortcode is C-12345
shortcode = input("Enter the Instagram shortcode: ")

try:
    # Obtain post metadata from the shortcode
    post = instaloader.Post.from_shortcode(L.context, shortcode)
    
    # Download the post (this handles videos and saves them to a new folder)
    L.download_post(post, target=shortcode)
    print("Video downloaded successfully!")
        
except Exception as e:
    print(f"An error occurred: {e}")
