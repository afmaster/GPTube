from utils import openaai_tricks, youtube_digest
import langid


def create_youtube_summary(user_input: str) -> str:
    """
    Create a summary of a YouTube video using the GPT model.
    :param user_input: The user input containing the YouTube URL.
    :return: The summary of the YouTube video.
    """
    url = youtube_digest.parse_url(user_input)
    if url is None:
        return "Vídeo não encontrado"
    video_id = youtube_digest.define_video_id(url)
    title = youtube_digest.fetch_title_from_youtube(video_id)
    lang = langid.classify(user_input)[0]
    text_to_ai = youtube_digest.create_youtube_summary_prompt(url, title, lang)
    response = openaai_tricks.create_completion(text_to_ai)
    return response


if __name__ == "__main__":
    user_input = "Resuma o vídeo https://www.youtube.com/watch?v=mW8T6O3cLWA"
    r = create_youtube_summary(user_input)
    print(r)
