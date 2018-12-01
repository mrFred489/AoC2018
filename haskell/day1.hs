import Data.List
import qualified Data.IntSet as S
import System.IO

-- input = do
--   text <- readFile "input1.txt"
--   lines text


readInts :: String -> [Int]
readInts = map (read . filter (/= '+')) . lines

modify :: Int -> Int -> Int
modify n change = n + change

part2 :: [Int] -> Maybe Int
part2 = go S.empty 0 . cycle
  where
    go set n changes
      | S.member n set = Just n
      | otherwise      = case changes of
          []     -> Nothing
          (x:xs) -> go (S.insert n set) (modify n x) xs


main = do
  input <- readFile "input1.txt"
  print $ (sum . readInts) input
  print $ part2 (readInts input)
