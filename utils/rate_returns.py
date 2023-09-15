#!/usr/bin/python3


def return_on_investment(initial_value, final_value):
    """ calculates the ROI of an investment
        Args:
            initial_value: initial amount invested
            final_value: current value of the investment
        Returns:
            change in the investment in decimal - 0.67
    """

    roi = (final_value - initial_value) / initial_value

    return roi

def time_weighted_return(*args):
    """ calculates the time weighted return of an investement taking into account cashflows
        Args:
            *args: roi of an investment of a given period in decimal - 0.56, 0.05
        Returns:
            return of the portfolio for the period in question
    """

    weighted_return = 1

    for arg in args:
        weighted_return *= (1 + arg)

    return weighted_return - 1
