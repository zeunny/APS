import Foundation

func solution(_ n:Int, _ arr1:[Int], _ arr2:[Int]) -> [String] {
    var answer: [String] = []
    
    for (val1, val2) in zip(arr1, arr2) {
        var value: String = String(val1|val2, radix:2)
        while value.count < n {
            value = "0" + value
        }
        value = value.replacingOccurrences(of: "1", with: "#")
        value = value.replacingOccurrences(of: "0", with: " ")
        answer.append(value)
    }
    
    return answer
}
