import UIKit

func solution(_ a:Int, _ b:Int) -> Int64 {
    var answer: Int64 = 0
    let min: Int = a > b ? b : a
    let max: Int = a > b ? a : b

    for i in min...max {
        answer += Int64(i)
    }
    
    return answer
}
