import Data.List
import qualified Data.IntSet as S
import System.IO
import Data.Map


strToFreq :: String -> [(Char, Int)]
strToFreq str = (toList $ fromListWith (+) [(c, 1) | c <- str])

mySnd :: (Char, Int) -> Int
mySnd inpu = snd inpu

myFilter :: Int -> Bool
myFilter val = case val of
  1 -> False
  _ -> True

strToNums :: String -> [Int]
strToNums inp = Data.List.filter myFilter (Data.List.nub (Data.List.map mySnd (strToFreq inp)))

numIfElem :: Int -> [Int] -> Int
numIfElem num xs = case (elem num xs) of
  True -> 1
  False -> 0

sumTwosThrees :: (Int, Int) -> [[Int]] -> (Int, Int)
sumTwosThrees acc xss =
      case xss of
        (x:xs) -> sumTwosThrees ((fst acc) + (numIfElem 2 x), (snd acc) + (numIfElem 3 x)) xs
        _ -> acc


part1 :: String -> (Int, Int) -- [Int]
part1 inp = sumTwosThrees (0,0) (Data.List.map strToNums (lines inp))


-- https://stackoverflow.com/questions/940382/what-is-the-difference-between-dot-and-dollar-sign
{-
list comprehension generating pairs with only one error

l and r iterates over the lines in the input

zip strings together so we get pairs of letters

filter above list to get only the pairs that is not equal

check if the length of the filtered list is 1

https://www.reddit.com/r/adventofcode/comments/a2aimr/2018_day_2_solutions/eawjtx9/
-}
part2 :: [String] -> [(String, String)]
part2 input = [(l, r) | l <- input, r <- input, (length . Data.List.filter (\(l,r) -> l /= r) $ Data.List.zip l r) == 1]


main = do
  input <- readFile "../input2.txt"
  print $ Data.List.zip "1234" "1244"
  print $ Data.List.filter (\(l,r) -> l /= r) [('1', '1'), ('1','2')]
  print $ ((fst (part1 input)) * (snd (part1 input)))
  print $ part2 $ lines input
