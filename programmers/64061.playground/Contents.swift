import Foundation

func solution(_ board:[[Int]], _ moves:[Int]) -> Int {
    var board: [[Int]] = board
    var answer: Int = 0
    var stack: [Int] = [Int]()
    
    for move in moves {
        var value = 0
        for i in 0..<board.count {
            if board[i][move-1] != 0 {
                value = board[i][move-1]
                board[i][move-1] = 0
                break
            }
        }
        
        if value != 0 {
            if !stack.isEmpty && value == stack[stack.index(before: stack.endIndex)] {
                answer += 2
                stack.removeLast()
            } else {
                stack.append(value)
            }
        }
    }
    
    return answer
}
