let inputSequence = "AAAACCCGGT"


let complement (nucleotide: char) = 
    match nucleotide with
    | 'A' -> 'T'
    | 'C' -> 'G'
    | 'G' -> 'C'
    | 'T' -> 'A'
    | _ -> '?'


let outputSequence = inputSequence
                        |> List.ofSeq
                        |> List.map complement
                        |> List.rev
                        |> System.String.Concat

printfn "%A" outputSequence