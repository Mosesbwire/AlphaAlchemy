#!/usr/bin/python3


import models

from models.transaction import Transaction


class TransactionService:

    def create(self,item, item_id, price, quantity, transaction_type, total, portfolio):
        transaction = Transaction(item, item_id,price, quantity, transaction_type, total)

        portfolio.transactions.append(transaction)

        return {"transaction": transaction, "error": None}
