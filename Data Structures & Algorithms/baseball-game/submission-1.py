class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # Store records
        record = []
        # Loop through operations
        for i in range(len(operations)):
            # Add previous 2 scores
            if operations[i] == "+":
                record.append(record[-1] + record[-2])
            # Delete last score
            elif operations[i] == "C":
                record.pop()
            # Double previous score
            elif operations[i] == "D":
                record.append(record[-1] * 2)
            # Add all numbers
            else:
                record.append(int(operations[i]))
        # return sum of scores
        return sum(record)

#Time: O(N)
#Space O(N)
        


        