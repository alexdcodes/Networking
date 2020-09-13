Clear-Host

$command1 = "show cdp neighbors"

$command2 = "show mac address-table"

$command3 = "show int desc"

$command4 = "show ver | i bin"

$command5 = "show switch"

$command6 = "show logging"

$command7 = "show spanning-tree blockedports"

$command8 = "show interfaces status err-disabled"

$command9 = "show switch"

$command10 = "show logging"

function SSH_execute (){

    Write-Host "`n Meh Health Check Automation `n`n Purpose: run Set of commands against router/switch"

#    Write-Host "`n`n`nConfiguration Settings`n"
    
 #   Write-Host "`n* Specify the Directory to Device-List.CSV "

 #   $dir_devicelist = Read-Host -Prompt "`n* Directory for Device List device-list.csv (ie: \\Client\C$\Temp\Healthcheck_alpha) "

 #   Write-Host "`n Specifiy the Full Path to log file save directory "

 #   $dir_log = Read-Host -Prompt "`n* Directory for Log File(s) (ie: \\Client\C$\Temp\Healthcheck_alpha\log) "


    Write-Host "`nLogin`n"

    $Global:username = Read-Host -Prompt "Enter your username " 

    $password = Read-Host -Prompt "Enter your password " 



    Import-Module SSH-sessions

   

    $DeviceList = Import-Csv "\\Client\C$\Temp\Healthcheck_alpha\device-list.csv" -Header "IPAddress"

    foreach ($IP_add in $Devicelist)

    {

    try{


        $Global:hostname = $IP_add.IPAddress;

        Remove-SshSession -RemoveAll -Verbose $hostname
     
        New-Sshsession -computername $hostname -username $username -password $password -ErrorAction Continue

        $Global:Resulta = Invoke-SshCommand -InvokeOnAll -Command $command1

        Start-Sleep 2 

        New-Sshsession -computername $hostname -username $username -password $password -ErrorAction Continue

        $Global:Result0 = Invoke-SshCommand -InvokeOnAll -Command $command2

        Start-Sleep 2 

        New-Sshsession -computername $hostname -username $username -password $password -ErrorAction Continue

        $Global:Result1 = Invoke-SshCommand -InvokeOnAll -Command $command3

        Start-Sleep 2 

        New-Sshsession -computername $hostname -username $username -password $password -ErrorAction Continue
    
        $Global:Result2 = Invoke-SshCommand -InvokeOnAll -Command $command4

        Start-Sleep 2 

        New-Sshsession -computername $hostname -username $username -password $password -ErrorAction Continue

        $Global:Result3 = Invoke-SshCommand -InvokeOnAll -Command $command5

        Start-Sleep 2 

        New-Sshsession -computername $hostname -username $username -password $password -ErrorAction Continue

        $Global:Result4 = Invoke-SshCommand -InvokeOnAll -Command $command6

        Start-Sleep 2 

        New-Sshsession -computername $hostname -username $username -password $password -ErrorAction Continue

        $Global:Result5 = Invoke-SshCommand -InvokeOnAll -Command $command7

        Start-Sleep 2 

        New-Sshsession -computername $hostname -username $username -password $password -ErrorAction Continue

        $Global:Result6 = Invoke-SshCommand -InvokeOnAll -Command $command8

        Start-Sleep 2 

        New-Sshsession -computername $hostname -username $username -password $password -ErrorAction Continue

        $Global:Result7 = Invoke-SshCommand -InvokeOnAll -Command $command9

        Start-Sleep 2 

        New-Sshsession -computername $hostname -username $username -password $password -ErrorAction Continue

        $Global:Result8 = Invoke-SshCommand -InvokeOnAll -Command $command10

        Remove-SshSession -RemoveAll -Verbose $hostname

 

        "+ Command Executed: $command1", "**********", $Resulta, " + Command Executed: $command2", "**********", $Result0, 
        
        "+ Command Executed: $command3", "**********", $Result1, "+ Command Executed: $command4","**********", $Result2, "+ Command Executed: $command5","**********", $Result3,

        "+ Command Executed: $command6","**********", $Result4, "+ Command Executed: $command7","**********", $Result5, "+ Command Executed: $command8","**********", $Result6,
        
        "+ Command Executed: $command9","**********", $Result7, "+ Command Executed: $command10","**********", $Result8,
    
        $Result8 | Out-File -FilePath "\\Client\C$\Temp\Healthcheck_alpha\log\$Global:hostname-$Global:username.txt" -encoding ASCII -Append 
           

   }

   catch {

    "+ Command Executed: $command1", "**********", $Resulta, " + Command Executed: $command2", "**********", $Result0, 
        
    "+ Command Executed: $command3", "**********", $Result1, "+ Command Executed: $command4","**********", $Result2, "+ Command Executed: $command5","**********", $Result3,

    "+ Command Executed: $command6","**********", $Result4, "+ Command Executed: $command7","**********", $Result5, "+ Command Executed: $command8","**********", $Result6,
    
    "+ Command Executed: $command9","**********", $Result7, "+ Command Executed: $command10","**********", $Result8,

    $Result8 | Out-File -FilePath "\\Client\C$\Temp\Healthcheck_alpha\log\$Global:hostname-$Global:username.ERROR.txt" -Append 

    Continue

   }

}


}

function excelCreate(){

    try {

        Write-Host "`nINFO: Creating Excel Log File`n"

        $excel = New-Object -ComObject excel.application

        $workbook = $excel.Workbooks.Add()

        $workbook_create = $workbook.Worksheets.Item(1)

        $workbook_create.Name = "log(1)"

        $workbook_create.Cells.Item(1,1) = "Device: $Global:hostname      Username: $Global:username"

        $workbook_create.Cells.Item(2,1) = "Check(1)"

        $workbook_create.Cells.Item(2,3) = "Check(2)"

        $workbook_create.Cells.Item(3,1) = "Commands:"

        $workbook_create.Cells.Item(4,1) = $command1 

        $workbook_create.Cells.Item(5,1) = $command2 

        $workbook_create.Cells.Item(6,1) = $command3

        $workbook_create.Cells.Item(7,1) = $command4

        $workbook_create.Cells.Item(8,1) = $command5

        $workbook_create.Cells.Item(9,1) = $command6

        $workbook_create.Cells.Item(10,1) = $command7

        $workbook_create.Cells.Item(11,1) = $command8

        $workbook_create.Cells.Item(12,1) = $command9

        $workbook_create.Cells.Item(13,1) = $command10

        $workbook_create.Cells.Item(4,2) = $Global:Resulta

        $workbook_create.Cells.Item(5,2) = $Global:Result0 

        $workbook_create.Cells.Item(6,2) = $Global:Result1 

        $workbook_create.Cells.Item(7,2) = $Global:Result2 

        $workbook_create.Cells.Item(8,2) = $Global:Result3 

        $workbook_create.Cells.Item(9,2) = $Global:Result4
        
        $workbook_create.Cells.Item(10,2) = $Global:Result5

        $workbook_create.Cells.Item(11,2) = $Global:Result6

        $workbook_create.Cells.Item(12,2) = $Global:Result7

        $workbook_create.Cells.Item(13,2) = $Global:Result8


# Merge Title Cells

        $MergeCells = $workbook_create.Range("A1:B1")

        $MergeCells2 = $workbook_create.Range("A2:B2")

        $MergeCells3 = $workbook_create.Range("A3:B3")

        $MergeCells4 = $workbook_create.Range("C2:D2")

        $MergeCells.Select()

        $MergeCells.MergeCells = $true

        $MergeCells2.Select()

        $MergeCells2.MergeCells = $true

        $MergeCells3.Select()

        $MergeCells3.MergeCells = $true

        $MergeCells4.Select()

        $MergeCells4.MergeCells = $true

        $workbook_create.Cells(1,1).HorizontalAlignment = -4108

        $workbook_create.Cells(2,1).HorizontalAlignment = -4108

        $workbook_create.Cells(3,1).HorizontalAlignment = -4108

        $workbook_create.Cells(2,3).HorizontalAlignment = -4108


#Format Workbook

        $excel_file ="\\Client\C$\Temp\log\$Global:hostname-$Global:username.xlsx"

        $workbook_create.Cells.Item(1,1).Font.Bold = $True

        $workbook_create.Cells.Item(2,1).Font.Bold = $True

        $workbook_create.Cells.Item(3,1).Font.Bold = $True

        $workbook_create.Cells.Item(2,3).Font.Bold = $True

    #    $workbook_create.Cells.Item(3,1).Font.Color = 255 #COLOR CODE FONT RED -- for changes

        $usedRange = $workbook_create.UsedRange

        $usedRange.EntireColumn.AutoFit() | Out-Null 

        $workbook.SaveAs($excel_file)

        $excel.Quit()

        Write-Host "`nSUCCESS: Excel (log) File Created $excel_file.`n"

    }

    catch {
        
        Write-Host "`nWARNING: Error Excel (log) file not created`n"

    }

    continue
    
}

function cleanupMOTD(){


    $removeString = Get-Content -Path "\\Client\C$\Temp\Healthcheck_alpha\inc\r"

    $rawFile = Get-Content -Path "\\Client\C$\Temp\Healthcheck_alpha\log\$Global:hostname-$Global:username.txt" | ForEach-Object {

        if ($_ -notin $removeString) { $_ }

    }

    Set-Content -Path "\\Client\C$\Temp\Healthcheck_alpha\log\$Global:hostname-$Global:username.txt" -Value $rawFile -Encoding Ascii

}



SSH_execute
#excelCreate
cleanupMOTD

