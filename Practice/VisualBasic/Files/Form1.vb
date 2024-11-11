
Imports System.IO

Public Class Form1

    Private Sub BtnOpen_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles BtnOpen.Click
        Dim FileReader As StreamReader
        Dim results As DialogResult
        results = OpenFileDialog1.ShowDialog
        If results = DialogResult.OK Then
            FileReader = New StreamReader(OpenFileDialog1.FileName)
            TextBox1.Text = FileReader.ReadToEnd()
            FileReader.Close()
        End If
    End Sub

    Private Sub BtnSave_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles BtnSave.Click
        Dim FileWriter As StreamWriter
        Dim results As DialogResult

        'Running into an issue where the saved file is coming out as a "File" format and not a text document 
        'Trying to find a way to default the extension to be a txt file 
        SaveFileDialog1.DefaultExt = "txt"

        results = SaveFileDialog1.ShowDialog
        If results = DialogResult.OK Then
            FileWriter = New StreamWriter(SaveFileDialog1.FileName, False)
            FileWriter.Write(TextBox1.Text)
            FileWriter.Close()
        End If
    End Sub

    Private Sub BtnClose_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles BtnClose.Click
        End
    End Sub

    Private Sub Button1_Click(sender As Object, e As EventArgs) Handles BtnOpen.Click

    End Sub
End Class
