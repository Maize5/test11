#!/usr/bin/env python3
#-*- coding: utf-8 -*-

class Account(object):
	"""
	账号类
	amount是美元金额
	"""
	def __init__(self, rate):
		self.__amt = 0
		self.rate = rate

	@property
	def amount(self):
		"""账号余额（美元）"""
		return self.__amt
		print("amount")

	@property
	def cny(self):
		"""账号余额（人民币）"""
		return self.__amt * self.rate
		print("执行到cny装饰器")

	@amount.setter
	def amount(self, value):
		if value < 0:
			print("Sorry, no negative amount in the account.")
			return
		self.__amt = value
		print("amount.setter")

if __name__ == '__main__':
	acc = Account(rate = 6.6)
	acc.amount = 20
	print("Dollar amount:", acc.amount)
	print("In CNY:", acc.cny)
	acc.mount = -100
	print("Dollar amount:", acc.amount)
