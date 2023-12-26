function Play-UltimateNumberGame {
    $min = 1
    $max = 100
    $secretNumber = Get-Random -Minimum $min -Maximum $max
    $guess = 0
    $attempts = 0

    Write-Host "我已經選好一個數字，範圍在 $min 到 $max 之間"

    while ($guess -ne $secretNumber) {
        $guess = Read-Host "請輸入你的號碼"
        if ( -not[int]::TryParse( $guess, [ref]0)){
            Write-Host "請輸入一個有效的數字"
            continue
        }

        $attempts++
        if ($guess -lt $secretNumber) {
            Write-Host "太低了"
        } elseif ($guess -gt $secretNumber) {
            Write-Host "太高了"
        }
    }
    Write-Host "恭喜你答對了，數字是 $secretNumber ，你總共猜了 $attempts 次"
}

# 運行遊戲
Play-UltimateNumberGame