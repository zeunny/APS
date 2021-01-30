import UIKit

func solution(_ n:Int) -> String {
    var answer: String = ""

    for _ in 0..<n/2 {
        answer += "수박"
    }
    
    if (n % 2 == 1) {
        answer += "수"
    }
    
    return answer
}
