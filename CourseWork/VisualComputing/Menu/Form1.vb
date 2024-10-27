Public Class frmMenuTab
    Private Sub CloseToolStripMenuItem_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles CloseToolStripMenuItem.Click
        Me.Close()
    End Sub
    Private Sub optBlack_CheckedChanged(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles optBlack.CheckedChanged
        displayLabel.ForeColor = Color.Black
    End Sub
    Private Sub optRed_CheckedChanged(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles optRed.CheckedChanged
        displayLabel.ForeColor = Color.Red
    End Sub
    Private Sub optGreen_CheckedChanged(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles optGreen.CheckedChanged
        displayLabel.ForeColor = Color.Green
    End Sub
    Private Sub opt12_CheckedChanged(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles opt12.CheckedChanged
        displayLabel.Font = New Font(displayLabel.Font.Name, 12)
    End Sub
    Private Sub opt16_CheckedChanged(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles opt16.CheckedChanged
        displayLabel.Font = New Font(displayLabel.Font.Name, 16)
    End Sub
    Private Sub opt20_CheckedChanged(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles opt20.CheckedChanged
        displayLabel.Font = New Font(displayLabel.Font.Name, 20)
    End Sub
    Private Sub optHello_CheckedChanged(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles optHello.CheckedChanged
        displayLabel.Text = "Hello!"
    End Sub
    Private Sub optGoodbye_CheckedChanged(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles optGoodbye.CheckedChanged
        displayLabel.Text = "Goodbye!"
    End Sub
    Private Sub BlackToolStripMenuItem_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles BlackToolStripMenuItem.Click
        displayLabel.ForeColor = Color.Black
    End Sub
    Private Sub RedToolStripMenuItem_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles RedToolStripMenuItem.Click
        displayLabel.ForeColor = Color.Red
    End Sub
    Private Sub GreenToolStripMenuItem_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles GreenToolStripMenuItem.Click
        displayLabel.ForeColor = Color.Green
    End Sub
    Private Sub ToolStripMenuItem2_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles ToolStripMenuItem2.Click
        displayLabel.Font = New Font(displayLabel.Font.Name, 12)
    End Sub
    Private Sub ToolStripMenuItem3_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles ToolStripMenuItem3.Click
        displayLabel.Font = New Font(displayLabel.Font.Name, 16)
    End Sub

    Private Sub ToolStripMenuItem4_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles ToolStripMenuItem4.Click
        displayLabel.Font = New Font(displayLabel.Font.Name, 20)
    End Sub
    Private Sub HelloToolStripMenuItem_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles HelloToolStripMenuItem.Click
        displayLabel.Text = "Hello!"
    End Sub
    Private Sub GoodbyeToolStripMenuItem_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles GoodbyeToolStripMenuItem.Click
        displayLabel.Text = "Goodbye!"
    End Sub
    Private Sub DeleteToolStripMenuItem_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles DeleteToolStripMenuItem.Click
        displayLabel.Text = " "
    End Sub
    Private Sub ExitToolStripMenuItem_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles ExitToolStripMenuItem.Click
        Application.Exit()
    End Sub
    Private Sub frmMenuTab_Load(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles MyBase.Load
    End Sub
End Class
