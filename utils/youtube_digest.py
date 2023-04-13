import requests


def fetch_title_from_youtube(video_id: str) -> str or None:
    """
    Fetch the title of a YouTube video given its video ID.
    :param video_id: The video ID of the YouTube video.
    :return: The title of the video, or None if not found.
    """
    url_to_fetch = f"https://noembed.com/embed?url=https://www.youtube.com/watch?v={video_id}"
    response = requests.get(url_to_fetch)
    data_dict = response.json()
    title = data_dict.get('title')
    return title


def define_video_id(url: str) -> str:
    """
    Extract the video ID from a YouTube URL.
    :param url: The YouTube video URL.
    :return: The video ID.
    """
    video_id = url.split("/")[-1]
    return video_id


def parse_url(user_input: str) -> str:
    """
    Parse the user input to extract the YouTube URL.
    :param user_input: The user input containing the YouTube URL.
    :return: The parsed YouTube URL.
    """
    tokens_list = user_input.split(" ")
    youtube_key_list = [
        'youtu',
        'http'
    ]
    match_list = [token for token in tokens_list if (any(item in token for item in youtube_key_list) and "/" in token)]
    url = match_list[0].rstrip(".").rstrip(",").rstrip("!").rstrip("?").strip().replace('watch?v=', '')
    return url


def create_youtube_summary_prompt(url: str, title: str, lang: str) -> str:
    """
    Create a prompt for the GPT model to summarize the YouTube video.
    :param url: The YouTube video URL.
    :param title: The title of the YouTube video.
    :param lang: The language of the summary.
    :return: The GPT model prompt for summarizing the video.
    """
    if 'en' in lang:
        text_to_ai = f"""
                Create a summary in English for the video: {url}
                Title: {title}
                """
    else:
        text_to_ai = f"""
                Crie um resumo em Português do vídeo: {url}
                Título: {title}
                """
    return text_to_ai



