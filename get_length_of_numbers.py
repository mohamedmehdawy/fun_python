    def getLength(number: int):
        """
          this function get the length of numbers
          parameters:
            number: the number should get length
           return: length of number
        """
        second_store = 0
        first_store = number
        step = 1
        counter = 0
        status = True
        

        # when number is zero
        if number == 0:
            return 1
        
        while status:
            
            # get the first number from right and store it in second store
            second_store += first_store % 10 * step
            step *= 10
            # remove the first number form right from first store
            first_store //= 10


            counter += 1
            # handel for divide by zero
            try:
                if number / second_store == 1:
                    status = False
            except:
                continue
        return counter
    
