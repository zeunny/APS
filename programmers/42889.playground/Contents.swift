import Foundation

func solution(_ N:Int, _ stages:[Int]) -> [Int] {
    var arrive_num: Double = Double(stages.count)
    var clear: [Double] = Array(repeating: 0, count: N+1)
    
    for stage in stages {
        if (stage < N+1) {
            clear[stage] += 1
        }
    }
    
    var fails: [(fail: Double, stage: Int)] = []
    for i in 1...N {
        fails.append((clear[i] / arrive_num, i))
        arrive_num -= clear[i]
    }
    
    fails.sort(by: {$0.fail > $1.fail})
    
    return fails.map{ $0.stage }
}
