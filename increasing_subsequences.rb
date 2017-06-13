# write a function that takes in an array and returns
# how many non-decreasing subranges there are
# ie for [1, 2, 3] there are 3, [1, 2], [2, 3], and [1, 2, 3]
# ie for [3, 1, 1] there is 1, [1, 1]

# brute force solution: enumerate all subsequences and
# iterate through them to test for non-decreasingness
def nondecreasing(array)
  subsequences = 0
  (0...array.length).each do |i|
    (i + 1...array.length).each do |j|
      nondecreasing = true
      p array[i..j]
      array[i..j].each_index do |k|
        if array[i + k + 1] && array[i + k] > array[i + k + 1]
          nondecreasing = false
          break
        end
      end
      if nondecreasing
        subsequences += 1
      end
    end
  end
  subsequences
end

p nondecreasing([1, 2, 3])
p nondecreasing([3, 1, 1])

# there is definitely repeated work to be done here. noteably
# that if a subsequence is already increasing or decreasing
# you only need to know the next value and the last value to determine
# if that's still true.

def quicksort(array)
  return array if array.length <= 1

  pivot = array.first
  left = array.drop(1).select { |el| el <= pivot }
  right = array.drop(1).select { |el| el > pivot }
  quicksort(left) + [pivot] + quicksort(right)
end

p quicksort([1, 3, 5, 2, 8, 1, 9, 0, 8, 1])
