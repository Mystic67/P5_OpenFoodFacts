#! /usr/bin/python3
# -*-coding: utf-8-*-


class Display_navigation:
    """This class takes the result of querie requests and
    allow to navigate in data """

    def __init__(self, result, step=8):
        self.result = result
        self.nb_of_results = len(result)
        self.row = 0
        self.step = step

    def increment_row(self):
        if self.nb_of_results == 0:
            self.row = self.row
        else:
            self.row = self.row + self.step
        return self.row

    def decrement_row(self):
        if self.row <= 0:
            self.row = 0
        else:
            self.row = self.row - self.step
        return self.row

    def reset_row(self):
        self.row = 0
        return self.row

    def get_max_results(self):
        return self.nb_of_results

    def get_products(self):
        product = self.result[self.row: (self.row + self.step)]
        return product

    def get_favorite(self):
        (prod, subst) = self.result[self.row]
        return (prod[0], subst[0])
