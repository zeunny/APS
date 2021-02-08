import Foundation

func solution(_ new_id:String) -> String {
    let lower: String = new_id.lowercased()
    
    let array_id: [Character] = Array(lower)
    var new_id: String = ""
    for t in array_id {
        if t.isNumber || t.isLetter || "-_.".contains(t) {
            new_id += String(t)
        }
    }
    
    while new_id.contains("..") {
        new_id = new_id.replacingOccurrences(of: "..", with: ".")
    }
    
    new_id = new_id.trimmingCharacters(in: ["."])
    
    if new_id.isEmpty {
        new_id = "a"
    }

    if new_id.count > 15 {
        let start = new_id.startIndex
        let end = new_id.index(new_id.startIndex, offsetBy: 14)
        new_id = String(new_id[start...end]).trimmingCharacters(in: ["."])
    }
    
    while new_id.count < 3 {
        new_id += String(new_id[new_id.index(before: new_id.endIndex)])
    }
    
    return new_id
}
