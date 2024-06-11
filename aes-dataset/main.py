import os
import base64
import pandas as pd
from base64 import b64encode
from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES
import json


class AesEncrypt(object):
	AES_COL = []
	PRIVATE_KEY = 'This is a key123'
	IV =  'This is an IV456'

	def __init__(self):
		pass

	# Load
	def load(self, file: str):
		df = file
		return df

	# Mapping
	def mapping(self, file: str, columns: list):
		loaded_data = self.load(file)
		selected_cols = loaded_data[columns]
		
		return selected_cols

	# Display
	def display_cols(self, file):
		df_display = self.load(file)
		print(df_display.columns.tolist())
	
	# Show
	def show(self, file, target):
		private_key = self.PRIVATE_KEY.encode('utf-8')
		iv = self.IV.encode('utf-8')
		cipher = AES.new(private_key, AES.MODE_CBC, iv)
		encrypted_cols = self.mapping(file, target).astype("str")

		for target in encrypted_cols:
			encrypted_words = cipher.encrypt(pad(target.encode('utf-8'), AES.block_size))
			self.AES_COL.append(b64encode(encrypted_words).decode('utf-8'))

		

		return self.AES_COL
