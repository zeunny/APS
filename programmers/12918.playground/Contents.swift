func solution(_ s:String) -> Bool {
    if (s.count != 4 && s.count != 6) {
        return false
    }
    
    for i in Array(s) {
        if (i.isLetter) {
            return false
        }
    }
    
    return true
}
