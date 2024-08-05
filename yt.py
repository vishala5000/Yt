import random

def generate_seo_title(titles):
    primary_title = "YouTube Video Title"
    all_titles = titles + [primary_title]
    seo_title = " | ".join(random.sample(all_titles, 3))
    return seo_title

def generate_seo_description(titles):
    emojis = ["🔥", "💡", "🚀", "👍", "🌟"]
    description = (
        f"{emojis[0]} Welcome to our video! Today we'll be discussing: {titles[0]}, {titles[1]}, {titles[2]}, {titles[3]}, {titles[4]}. "
        "Stay tuned as we dive deep into each topic and provide valuable insights and tips. "
        f"Don't forget to like, share, and subscribe for more awesome content! {emojis[1]} {emojis[2]}"
    )
    return description

def generate_hashtags(titles):
    hashtags = [f"#{title.replace(' ', '')}" for title in titles]
    return " ".join(hashtags)

def generate_seo_tags(titles):
    tags = [title.replace(' ', ',') for title in titles]
    return ",".join(tags)

def generate_thumbnail_prompt(titles):
    prompt = (
        f"Create an eye-catching YouTube thumbnail for a video titled: {titles[0]}, {titles[1]}, {titles[2]}, {titles[3]}, {titles[4]}. "
        "Include vibrant colors, bold text, and relevant imagery to attract viewers."
    )
    return prompt

def main():
    titles = []
    for i in range(1, 6):
        title = input(f"Enter title {i}: ")
        titles.append(title)
    
    seo_title = generate_seo_title(titles)
    seo_description = generate_seo_description(titles)
    hashtags = generate_hashtags(titles)
    seo_tags = generate_seo_tags(titles)
    thumbnail_prompt = generate_thumbnail_prompt(titles)
    
    print("\nSEO Optimized Title:\n", seo_title)
    print("\nSEO Optimized Description:\n", seo_description)
    print("\nHashtags:\n", hashtags)
    print("\nSEO Optimized Tags:\n", seo_tags)
    print("\nThumbnail Prompt:\n", thumbnail_prompt)

if __name__ == "__main__":
    main()
