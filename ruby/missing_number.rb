def missing_number1(arr1, arr2)
  arr1-arr2
end

def missing_number2(arr1,arr2)
  arr2 = arr2.sort
  counter = 0
  while (arr1[counter] == arr2[counter])
    counter +=1
  end
  puts arr1[counter]
end


missing_number2([1,2,3,4,5,6,7],[3,7,2,1,4,6])
