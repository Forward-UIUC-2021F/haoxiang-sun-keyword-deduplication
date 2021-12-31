import json
import os
import pandas as pd
import plotly.express as px

class VisualizeLoss:
	def __init__(self, config=None):
		self.config = config
		if config:
			self.read_data(config)

	def read_data(self, config):
		log_file_path = os.path.join(config['model_dir'], 'train_log.json')

		with open(log_file_path) as f:
			train_log = json.load(f)

		train_losses = train_log['train_losses']
		data = pd.DataFrame(train_losses[:60]).reset_index()
		data.columns = ['Epoch', 'Loss']

		self.training_loss = data

	def show(self, name):
		if name == 'train_loss':
			fig = px.line(self.training_loss, x='Epoch', y='Loss', title='Training Loss')
			return fig
