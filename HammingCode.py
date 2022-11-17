import numpy as np
from typing import Union

class HammingCode:
      '''
      
      Input a 4-bit binary value input to see Hamming's Code in action. 
      List or a one long int is accepted as input, as long as it only includes 4-bits.
      
      '''
      
      def __init__(self, bit_input: Union[int, list]):
            # if/else to accept two types of inputs. 
            if type(bit_input) == list:
                  self.bit_input = np.array(bit_input)
            else:
                  self.bit_input = np.array([int(x) for x in (str(bit_input))])
            
            # Error handling: If max bit > 1 or length bigger or smaller than 4, raise error
            if max(self.bit_input) > 1:
                  raise ValueError(f"Only takes binary values (1's or 0's). Your input included {max(self.bit_input)}")
            elif len(self.bit_input) != 4:
                  raise SyntaxError(f"Input can be no more than 4-bits. You inputted {len(self.bit_input)} bits")
            
            # Calling code_word method when object is initialized
            self.code_word_generator() 
            
      
      def code_word_generator(self):
            """
            Transforms the 4-bit input value to a 7-bit binary vector codeword.
            """
            self.code_word = self.bit_input
            
            self.parity_bits = {
                  #key = bit position (not at index 0), 
                  #value = encoded parity bit (placeholder).
                  1: [0 if (self.code_word[0] + self.code_word[1] + self.code_word[3])%2 == 0 else 1][0], #Using sum, to transform 
                  2: [0 if (self.code_word[0] + self.code_word[2] + self.code_word[3])%2 == 0 else 1][0],
                  4: [0 if (self.code_word[1] + self.code_word[2] + self.code_word[3])%2 == 0 else 1][0],
            }
            
            # Add parity values add the right index to form 7-bit vector code word
            for key in self.parity_bits:
                  self.code_word = np.insert(self.code_word, key-1, self.parity_bits[key])
      
      # Adding represent method for nicer output of codeword
      def __repr__(self):
            return f"7-bit codeword of input {str(self.bit_input)}: \n{str(self.code_word):-^34s}"
      
      
      def parity_check(self, test=False):
            ''' 
            Check if 4-bit input have been corrupted.
            
            test variable allows to deliberately corrupt a input, to see parity check on a corrupted input
            '''
            parity_check_matrix = np.array([[1,0,1,0,1,0,1],
                                            [0,1,1,0,0,1,1],
                                            [0,0,0,1,1,1,1]])
            
            if test == True:
                  disrupted_codeword = self.code_word.copy()
                  if disrupted_codeword[2] == 0:
                        disrupted_codeword[2] = 1
                  else:
                        disrupted_codeword[2] = 0
                  
                  parity_check_dot_product = parity_check_matrix.dot(disrupted_codeword)
                  
                  parity_check = np.mod(parity_check_dot_product, 2)
                  
                  return f'The data have been corrupted, as the parity check and modulo 2 oepration returns: {parity_check}'
            else:
                  parity_check_dot_product = parity_check_matrix.dot(self.code_word)
                  
                  parity_check = np.mod(parity_check_dot_product, 2)
                  
                  if max(parity_check) > 0:
                        return f'The data have been corrupted, as the parity check and modulo 2 oepration returns: {parity_check}'
                  else:
                        return f'The data have not been corrupted, as the parity check and modulo 2 oepration returns: {parity_check}'
