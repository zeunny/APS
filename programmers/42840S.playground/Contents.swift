import Foundation

func solution(_ answers:[Int]) -> [Int] {
    var answer: [Int] = []
    var scores: [(order: Int, score: Int)] = []
    let giveUpMath: [Int: [Int]] = [1: [1, 2, 3, 4, 5], 2: [2, 1, 2, 3, 2, 4, 2, 5], 3: [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    
    for key in giveUpMath.keys {
        var cnt: Int = 0
        for i in 0..<answers.count {
            if (giveUpMath[key]![i%(giveUpMath[key]!.count)] == answers[i]) {
                cnt += 1
            }
        }
        scores.append((key, cnt))
    }

    scores.sort(by: {$0.score > $1.score})
    answer.append(scores[0].order)
    if (scores[0].score == scores[1].score) {
        answer.append(scores[1].order)
    }
    if (scores[0].score == scores[2].score) {
        answer.append(scores[2].order)
    }
    
    answer.sort()
    
    return answer
}
