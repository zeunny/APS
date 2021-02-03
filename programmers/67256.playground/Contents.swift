import Foundation

func solution(_ numbers:[Int], _ hand:String) -> String {
    var result: String = ""
    let position: [String: (Int, Int)] = ["1": (0, 0), "2": (0, 1), "3": (0, 2),
                                          "4": (1, 0), "5": (1, 1), "6": (1, 2),
                                          "7": (2, 0), "8": (2, 1), "9": (2, 2),
                                          "*": (3, 0), "0": (3, 1), "#": (3, 2)]

    var leftCurrent: String = "*"
    var rightCurrent: String = "#"
    
    for number in numbers {
        if number == 1 || number == 4 || number == 7 {
            result += "L"
            leftCurrent = String(number)
        } else if number == 3 || number == 6 || number == 9 {
            result += "R"
            rightCurrent = String(number)
        } else {
            let strNum: String = String(number)
            
            let leftCount: Int = abs(position[strNum]!.0 - position[leftCurrent]!.0) + abs(position[strNum]!.1 - position[leftCurrent]!.1)
            let rightCount: Int = abs(position[strNum]!.0 - position[rightCurrent]!.0) + abs(position[strNum]!.1 - position[rightCurrent]!.1)

            if leftCount > rightCount {
                result += "R"
                rightCurrent = strNum
            } else if leftCount < rightCount {
                result += "L"
                leftCurrent = strNum
            } else {
                result += hand[hand.startIndex].uppercased()
                if hand == "left" {
                    leftCurrent = strNum
                } else {
                    rightCurrent = strNum
                }
            }
        }
    }
    
    return result
}
