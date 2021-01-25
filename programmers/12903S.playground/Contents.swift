import UIKit

func solution(_ s:String) -> String {
    if (s.count % 2 == 1) {
        return "\(s[s.index(s.startIndex, offsetBy: s.count/2)])"
    } else {
        return "\(s[s.index(s.startIndex, offsetBy: s.count/2-1)])" + "\(s[s.index(s.startIndex, offsetBy: s.count/2)])"
    }
}
