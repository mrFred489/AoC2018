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

sumTwosThrees :: (Int, Int) -> [[Int]] -> (Int, Int)
sumTwosThrees acc xss =
      case xss of
        (x:xs) -> case x of
          [2]    -> sumTwosThrees ((fst acc) + 1, snd acc) xs
          [3]    -> sumTwosThrees (fst acc, (snd acc) + 1) xs
          [2, 3] -> sumTwosThrees ((fst acc) + 1, (snd acc) + 1) xs
          [3,2] -> sumTwosThrees ((fst acc) + 1, (snd acc) + 1) xs
          _      -> sumTwosThrees acc xs
        _ -> acc


part1 :: String -> (Int, Int) -- [Int]
part1 inp = sumTwosThrees (0,0) (Data.List.map strToNums (lines inp))


main = do
  input <- readFile "../input2.txt"
  print $ strToFreq input
  print $ strToNums input
  print $ part1 input
  print $ ((fst (part1 input)) * (snd (part1 input)))
