# Load

Time complexity = O(N), where `N` is the length of the string.

* First step is to split the input on newlines - O(N) operation
* Next step is to split each of the substrings on `;` - again O(L * K), where `L` - length of the substring, K - count of substrings.
  Since all the substrings added together still form original string, O(L * K) == O(N)
* Third step is to split each key-value pair on `=` - same observation, O(N) complexity

Space complexity - O(N), with the similar proof.

*NB:* a more efficient, yet less clean solution could be designed, still with O(N) asymptotic complexity, but smaller quotients.

# Store

Time complexity = O(N*M), where `N` is number of lists, `M` - number of items in the map.
   
Obviously, each key-value pair is touched once and each list is touched once as well. 

Space complexity - O(N * M), with the similar proof