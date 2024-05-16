from gradio_client import Client, file

client = Client("http://localhost:5003/")
result = client.predict(
		lang="vi",
		tts_text="Xin chào, tôi là một công cụ chuyển đổi văn bản thành giọng nói tiếng Việt được phát triển bởi nhóm Nón lá.",
		speaker_audio_file=file('Recording_4.wav'),
		use_deepfilter=False,
		normalize_text=True,
		api_name="/run_tts"
)
print(result)