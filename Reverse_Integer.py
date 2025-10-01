class Solution:
    def reverse(self, x: int) -> int:
        def is_outside_32bit_signed(n):
            return n < -2_147_483_648 or n > 2_147_483_647
        x = str(x)
        if x[0] == "-":
            x = x[1:][::-1]
            x = "-"+x
            print(x)
        else:
            x = x[::-1]
        x = int(x)
        if is_outside_32bit_signed(x) == False:
            return x
        else:
            return 0

        # optimal solution and works