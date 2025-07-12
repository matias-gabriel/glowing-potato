class Solution:
    def do_calc(self, n_1, n_2, operation):
      if operation == "+":
        return n_1 + n_2
      elif operation == "-":
        return n_1 - n_2
      elif operation == "/":
        return int(n_1 / n_2)
      elif operation == "*":
        return n_1 * n_2

    def is_int(self, i):
      try:
        int(i)
        return True
      except:
        False

    def evalRPN(self, tokens: List[str]) -> int:
      numbers_stack = []

      for i in tokens:
        if self.is_int(i):
          numbers_stack.append(int(i))
        else:
          n_2 = numbers_stack.pop()
          n_1 = numbers_stack.pop()
          value = self.do_calc(n_1, n_2, i)
          numbers_stack.append(value)

      return numbers_stack.pop()
        