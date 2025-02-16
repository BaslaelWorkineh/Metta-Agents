!("AFImportanceDiffusionAgent.metta")
! ((py-atom time.sleep) 1)
!("AFImportanceDiffusionAgent.metta")

(x 1)

(= (adder $x)
    (add-atom &self (x (+ $x 1)))
)

!(adder 1)
!(match &self (x $num) $num)
