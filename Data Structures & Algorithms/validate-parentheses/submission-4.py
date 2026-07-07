class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        for ch in s:

            # If opening bracket, push it
            if ch == "(" or ch == "[" or ch == "{":
                stack.append(ch)

            # Otherwise it is a closing bracket
            else:

                # If stack is empty, there is nothing to match
                if not stack:
                    return False

                # Check matching brackets
                if ch == ")" and stack[-1] == "(":
                    stack.pop()

                elif ch == "]" and stack[-1] == "[":
                    stack.pop()

                elif ch == "}" and stack[-1] == "{":
                    stack.pop()

                else:
                    return False

        # At the end, stack should be empty
        return len(stack) == 0
            
        
        