<Global.Microsoft.VisualBasic.CompilerServices.DesignerGenerated()> _
Partial Class simpleEvent
    Inherits System.Windows.Forms.Form

    'Form overrides dispose to clean up the component list.
    <System.Diagnostics.DebuggerNonUserCode()> _
    Protected Overrides Sub Dispose(ByVal disposing As Boolean)
        Try
            If disposing AndAlso components IsNot Nothing Then
                components.Dispose()
            End If
        Finally
            MyBase.Dispose(disposing)
        End Try
    End Sub

    'Required by the Windows Form Designer
    Private components As System.ComponentModel.IContainer

    'NOTE: The following procedure is required by the Windows Form Designer
    'It can be modified using the Windows Form Designer.  
    'Do not modify it using the code editor.
    <System.Diagnostics.DebuggerStepThrough()> _
    Private Sub InitializeComponent()
        Me.clickMeButton = New System.Windows.Forms.Button()
        Me.SuspendLayout()
        '
        'clickMeButton
        '
        Me.clickMeButton.Location = New System.Drawing.Point(105, 119)
        Me.clickMeButton.Name = "clickMeButton"
        Me.clickMeButton.Size = New System.Drawing.Size(75, 23)
        Me.clickMeButton.TabIndex = 0
        Me.clickMeButton.Text = "Click Me"
        Me.clickMeButton.UseVisualStyleBackColor = True
        '
        'simpleEvent
        '
        Me.AutoScaleDimensions = New System.Drawing.SizeF(6.0!, 13.0!)
        Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
        Me.ClientSize = New System.Drawing.Size(284, 261)
        Me.Controls.Add(Me.clickMeButton)
        Me.Name = "simpleEvent"
        Me.Text = "Simple Event Example"
        Me.ResumeLayout(False)

    End Sub

    Friend WithEvents clickMeButton As Button
End Class
