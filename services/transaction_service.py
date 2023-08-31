#!/usr/bin/python3


import models

from models.transaction import Transaction


class TransactionService:

    def create(self,item, price, quantity, transaction_type, total, portfolio):
        transaction = Transaction(item, price, quantity, transaction_type, total)

        portfolio.transactions.append(transaction)

        return {"transaction": transaction, "error": None}
