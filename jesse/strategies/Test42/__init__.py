from jesse.strategies import Strategy


# test_is_increased
class Test42(Strategy):
    def should_long(self) -> bool:
        """

        :return:
        """
        return self.index == 0

    def should_short(self) -> bool:
        """

        :return:
        """
        return False

    def go_long(self):
        """

        """
        self.buy = [
            (.5, 2),
            (.5, 4),
        ]
        self.take_profit = [
            (.5, 6),
            (.5, 10),
        ]

    def update_position(self):
        """

        """
        if self.price < 4 and self.position.qty == .5:
            assert not self.is_increased
            assert not self.is_reduced

        if self.position.qty == 1:
            assert self.is_increased
            assert not self.is_reduced

    def go_short(self):
        """

        """
        pass

    def should_cancel(self):
        """

        :return:
        """
        return False
