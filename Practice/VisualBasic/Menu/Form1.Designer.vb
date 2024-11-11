<Global.Microsoft.VisualBasic.CompilerServices.DesignerGenerated()> _
Partial Class frmMenuTab
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
        Me.MenuStrip1 = New System.Windows.Forms.MenuStrip()
        Me.FileToolStripMenuItem = New System.Windows.Forms.ToolStripMenuItem()
        Me.CloseToolStripMenuItem = New System.Windows.Forms.ToolStripMenuItem()
        Me.ExitToolStripMenuItem = New System.Windows.Forms.ToolStripMenuItem()
        Me.EditToolStripMenuItem = New System.Windows.Forms.ToolStripMenuItem()
        Me.ColorToolStripMenuItem = New System.Windows.Forms.ToolStripMenuItem()
        Me.BlackToolStripMenuItem = New System.Windows.Forms.ToolStripMenuItem()
        Me.RedToolStripMenuItem = New System.Windows.Forms.ToolStripMenuItem()
        Me.GreenToolStripMenuItem = New System.Windows.Forms.ToolStripMenuItem()
        Me.SizeToolStripMenuItem = New System.Windows.Forms.ToolStripMenuItem()
        Me.ToolStripMenuItem2 = New System.Windows.Forms.ToolStripMenuItem()
        Me.ToolStripMenuItem3 = New System.Windows.Forms.ToolStripMenuItem()
        Me.ToolStripMenuItem4 = New System.Windows.Forms.ToolStripMenuItem()
        Me.DeleteToolStripMenuItem = New System.Windows.Forms.ToolStripMenuItem()
        Me.MessageToolStripMenuItem = New System.Windows.Forms.ToolStripMenuItem()
        Me.HelloToolStripMenuItem = New System.Windows.Forms.ToolStripMenuItem()
        Me.GoodbyeToolStripMenuItem = New System.Windows.Forms.ToolStripMenuItem()
        Me.TabControl1 = New System.Windows.Forms.TabControl()
        Me.TabPage1 = New System.Windows.Forms.TabPage()
        Me.optGreen = New System.Windows.Forms.RadioButton()
        Me.optRed = New System.Windows.Forms.RadioButton()
        Me.optBlack = New System.Windows.Forms.RadioButton()
        Me.TabPage2 = New System.Windows.Forms.TabPage()
        Me.opt20 = New System.Windows.Forms.RadioButton()
        Me.opt16 = New System.Windows.Forms.RadioButton()
        Me.opt12 = New System.Windows.Forms.RadioButton()
        Me.TabPage3 = New System.Windows.Forms.TabPage()
        Me.optGoodbye = New System.Windows.Forms.RadioButton()
        Me.optHello = New System.Windows.Forms.RadioButton()
        Me.displayLabel = New System.Windows.Forms.Label()
        Me.MenuStrip1.SuspendLayout()
        Me.TabControl1.SuspendLayout()
        Me.TabPage1.SuspendLayout()
        Me.TabPage2.SuspendLayout()
        Me.TabPage3.SuspendLayout()
        Me.SuspendLayout()
        '
        'MenuStrip1
        '
        Me.MenuStrip1.Items.AddRange(New System.Windows.Forms.ToolStripItem() {Me.FileToolStripMenuItem, Me.EditToolStripMenuItem, Me.MessageToolStripMenuItem})
        Me.MenuStrip1.Location = New System.Drawing.Point(0, 0)
        Me.MenuStrip1.Name = "MenuStrip1"
        Me.MenuStrip1.Size = New System.Drawing.Size(266, 24)
        Me.MenuStrip1.TabIndex = 0
        Me.MenuStrip1.Text = "MenuStrip1"
        '
        'FileToolStripMenuItem
        '
        Me.FileToolStripMenuItem.DropDownItems.AddRange(New System.Windows.Forms.ToolStripItem() {Me.CloseToolStripMenuItem, Me.ExitToolStripMenuItem})
        Me.FileToolStripMenuItem.Name = "FileToolStripMenuItem"
        Me.FileToolStripMenuItem.Size = New System.Drawing.Size(37, 20)
        Me.FileToolStripMenuItem.Text = "&File"
        '
        'CloseToolStripMenuItem
        '
        Me.CloseToolStripMenuItem.Name = "CloseToolStripMenuItem"
        Me.CloseToolStripMenuItem.ShortcutKeys = CType((System.Windows.Forms.Keys.Control Or System.Windows.Forms.Keys.C), System.Windows.Forms.Keys)
        Me.CloseToolStripMenuItem.Size = New System.Drawing.Size(180, 22)
        Me.CloseToolStripMenuItem.Text = "&Close"
        '
        'ExitToolStripMenuItem
        '
        Me.ExitToolStripMenuItem.Name = "ExitToolStripMenuItem"
        Me.ExitToolStripMenuItem.ShortcutKeys = CType((System.Windows.Forms.Keys.Control Or System.Windows.Forms.Keys.E), System.Windows.Forms.Keys)
        Me.ExitToolStripMenuItem.Size = New System.Drawing.Size(180, 22)
        Me.ExitToolStripMenuItem.Text = "&Exit"
        '
        'EditToolStripMenuItem
        '
        Me.EditToolStripMenuItem.DropDownItems.AddRange(New System.Windows.Forms.ToolStripItem() {Me.ColorToolStripMenuItem, Me.SizeToolStripMenuItem, Me.DeleteToolStripMenuItem})
        Me.EditToolStripMenuItem.Name = "EditToolStripMenuItem"
        Me.EditToolStripMenuItem.Size = New System.Drawing.Size(39, 20)
        Me.EditToolStripMenuItem.Text = "&Edit"
        '
        'ColorToolStripMenuItem
        '
        Me.ColorToolStripMenuItem.DropDownItems.AddRange(New System.Windows.Forms.ToolStripItem() {Me.BlackToolStripMenuItem, Me.RedToolStripMenuItem, Me.GreenToolStripMenuItem})
        Me.ColorToolStripMenuItem.Name = "ColorToolStripMenuItem"
        Me.ColorToolStripMenuItem.Size = New System.Drawing.Size(180, 22)
        Me.ColorToolStripMenuItem.Text = "&Color"
        '
        'BlackToolStripMenuItem
        '
        Me.BlackToolStripMenuItem.Name = "BlackToolStripMenuItem"
        Me.BlackToolStripMenuItem.ShortcutKeys = CType((System.Windows.Forms.Keys.Control Or System.Windows.Forms.Keys.B), System.Windows.Forms.Keys)
        Me.BlackToolStripMenuItem.Size = New System.Drawing.Size(180, 22)
        Me.BlackToolStripMenuItem.Text = "&Black"
        '
        'RedToolStripMenuItem
        '
        Me.RedToolStripMenuItem.Name = "RedToolStripMenuItem"
        Me.RedToolStripMenuItem.ShortcutKeys = CType((System.Windows.Forms.Keys.Control Or System.Windows.Forms.Keys.R), System.Windows.Forms.Keys)
        Me.RedToolStripMenuItem.Size = New System.Drawing.Size(180, 22)
        Me.RedToolStripMenuItem.Text = "&Red"
        '
        'GreenToolStripMenuItem
        '
        Me.GreenToolStripMenuItem.Name = "GreenToolStripMenuItem"
        Me.GreenToolStripMenuItem.ShortcutKeys = CType((System.Windows.Forms.Keys.Control Or System.Windows.Forms.Keys.G), System.Windows.Forms.Keys)
        Me.GreenToolStripMenuItem.Size = New System.Drawing.Size(180, 22)
        Me.GreenToolStripMenuItem.Text = "&Green"
        '
        'SizeToolStripMenuItem
        '
        Me.SizeToolStripMenuItem.DropDownItems.AddRange(New System.Windows.Forms.ToolStripItem() {Me.ToolStripMenuItem2, Me.ToolStripMenuItem3, Me.ToolStripMenuItem4})
        Me.SizeToolStripMenuItem.Name = "SizeToolStripMenuItem"
        Me.SizeToolStripMenuItem.Size = New System.Drawing.Size(180, 22)
        Me.SizeToolStripMenuItem.Text = "&Size"
        '
        'ToolStripMenuItem2
        '
        Me.ToolStripMenuItem2.Name = "ToolStripMenuItem2"
        Me.ToolStripMenuItem2.ShortcutKeys = CType((System.Windows.Forms.Keys.Control Or System.Windows.Forms.Keys.F12), System.Windows.Forms.Keys)
        Me.ToolStripMenuItem2.Size = New System.Drawing.Size(180, 22)
        Me.ToolStripMenuItem2.Text = "12"
        '
        'ToolStripMenuItem3
        '
        Me.ToolStripMenuItem3.Name = "ToolStripMenuItem3"
        Me.ToolStripMenuItem3.ShortcutKeys = CType((System.Windows.Forms.Keys.Control Or System.Windows.Forms.Keys.F16), System.Windows.Forms.Keys)
        Me.ToolStripMenuItem3.Size = New System.Drawing.Size(180, 22)
        Me.ToolStripMenuItem3.Text = "16"
        '
        'ToolStripMenuItem4
        '
        Me.ToolStripMenuItem4.Name = "ToolStripMenuItem4"
        Me.ToolStripMenuItem4.ShortcutKeys = CType((System.Windows.Forms.Keys.Control Or System.Windows.Forms.Keys.F20), System.Windows.Forms.Keys)
        Me.ToolStripMenuItem4.Size = New System.Drawing.Size(180, 22)
        Me.ToolStripMenuItem4.Text = "20"
        '
        'DeleteToolStripMenuItem
        '
        Me.DeleteToolStripMenuItem.Name = "DeleteToolStripMenuItem"
        Me.DeleteToolStripMenuItem.ShortcutKeys = CType((System.Windows.Forms.Keys.Control Or System.Windows.Forms.Keys.Delete), System.Windows.Forms.Keys)
        Me.DeleteToolStripMenuItem.Size = New System.Drawing.Size(180, 22)
        Me.DeleteToolStripMenuItem.Text = "&Delete"
        '
        'MessageToolStripMenuItem
        '
        Me.MessageToolStripMenuItem.DropDownItems.AddRange(New System.Windows.Forms.ToolStripItem() {Me.HelloToolStripMenuItem, Me.GoodbyeToolStripMenuItem})
        Me.MessageToolStripMenuItem.Name = "MessageToolStripMenuItem"
        Me.MessageToolStripMenuItem.Size = New System.Drawing.Size(65, 20)
        Me.MessageToolStripMenuItem.Text = "&Message"
        '
        'HelloToolStripMenuItem
        '
        Me.HelloToolStripMenuItem.Name = "HelloToolStripMenuItem"
        Me.HelloToolStripMenuItem.Size = New System.Drawing.Size(180, 22)
        Me.HelloToolStripMenuItem.Text = "&Hello!"
        '
        'GoodbyeToolStripMenuItem
        '
        Me.GoodbyeToolStripMenuItem.Name = "GoodbyeToolStripMenuItem"
        Me.GoodbyeToolStripMenuItem.Size = New System.Drawing.Size(180, 22)
        Me.GoodbyeToolStripMenuItem.Text = "&Goodbye!"
        '
        'TabControl1
        '
        Me.TabControl1.Controls.Add(Me.TabPage1)
        Me.TabControl1.Controls.Add(Me.TabPage2)
        Me.TabControl1.Controls.Add(Me.TabPage3)
        Me.TabControl1.Location = New System.Drawing.Point(0, 49)
        Me.TabControl1.Name = "TabControl1"
        Me.TabControl1.SelectedIndex = 0
        Me.TabControl1.Size = New System.Drawing.Size(266, 156)
        Me.TabControl1.TabIndex = 1
        '
        'TabPage1
        '
        Me.TabPage1.Controls.Add(Me.optGreen)
        Me.TabPage1.Controls.Add(Me.optRed)
        Me.TabPage1.Controls.Add(Me.optBlack)
        Me.TabPage1.Location = New System.Drawing.Point(4, 22)
        Me.TabPage1.Name = "TabPage1"
        Me.TabPage1.Padding = New System.Windows.Forms.Padding(3)
        Me.TabPage1.Size = New System.Drawing.Size(258, 130)
        Me.TabPage1.TabIndex = 0
        Me.TabPage1.Text = "Color"
        Me.TabPage1.UseVisualStyleBackColor = True
        '
        'optGreen
        '
        Me.optGreen.AutoSize = True
        Me.optGreen.Location = New System.Drawing.Point(8, 65)
        Me.optGreen.Name = "optGreen"
        Me.optGreen.Size = New System.Drawing.Size(54, 17)
        Me.optGreen.TabIndex = 2
        Me.optGreen.Text = "Green"
        Me.optGreen.UseVisualStyleBackColor = True
        '
        'optRed
        '
        Me.optRed.AutoSize = True
        Me.optRed.Location = New System.Drawing.Point(8, 42)
        Me.optRed.Name = "optRed"
        Me.optRed.Size = New System.Drawing.Size(45, 17)
        Me.optRed.TabIndex = 1
        Me.optRed.Text = "Red"
        Me.optRed.UseVisualStyleBackColor = True
        '
        'optBlack
        '
        Me.optBlack.AutoSize = True
        Me.optBlack.Checked = True
        Me.optBlack.Location = New System.Drawing.Point(8, 19)
        Me.optBlack.Name = "optBlack"
        Me.optBlack.Size = New System.Drawing.Size(52, 17)
        Me.optBlack.TabIndex = 0
        Me.optBlack.TabStop = True
        Me.optBlack.Text = "Black"
        Me.optBlack.UseVisualStyleBackColor = True
        '
        'TabPage2
        '
        Me.TabPage2.Controls.Add(Me.opt20)
        Me.TabPage2.Controls.Add(Me.opt16)
        Me.TabPage2.Controls.Add(Me.opt12)
        Me.TabPage2.Location = New System.Drawing.Point(4, 22)
        Me.TabPage2.Name = "TabPage2"
        Me.TabPage2.Padding = New System.Windows.Forms.Padding(3)
        Me.TabPage2.Size = New System.Drawing.Size(258, 130)
        Me.TabPage2.TabIndex = 1
        Me.TabPage2.Text = "Size"
        Me.TabPage2.UseVisualStyleBackColor = True
        '
        'opt20
        '
        Me.opt20.AutoSize = True
        Me.opt20.Location = New System.Drawing.Point(8, 64)
        Me.opt20.Name = "opt20"
        Me.opt20.Size = New System.Drawing.Size(37, 17)
        Me.opt20.TabIndex = 2
        Me.opt20.TabStop = True
        Me.opt20.Text = "20"
        Me.opt20.UseVisualStyleBackColor = True
        '
        'opt16
        '
        Me.opt16.AutoSize = True
        Me.opt16.Location = New System.Drawing.Point(8, 41)
        Me.opt16.Name = "opt16"
        Me.opt16.Size = New System.Drawing.Size(37, 17)
        Me.opt16.TabIndex = 1
        Me.opt16.TabStop = True
        Me.opt16.Text = "16"
        Me.opt16.UseVisualStyleBackColor = True
        '
        'opt12
        '
        Me.opt12.AutoSize = True
        Me.opt12.Location = New System.Drawing.Point(8, 18)
        Me.opt12.Name = "opt12"
        Me.opt12.Size = New System.Drawing.Size(37, 17)
        Me.opt12.TabIndex = 0
        Me.opt12.TabStop = True
        Me.opt12.Text = "12"
        Me.opt12.UseVisualStyleBackColor = True
        '
        'TabPage3
        '
        Me.TabPage3.Controls.Add(Me.optGoodbye)
        Me.TabPage3.Controls.Add(Me.optHello)
        Me.TabPage3.Location = New System.Drawing.Point(4, 22)
        Me.TabPage3.Name = "TabPage3"
        Me.TabPage3.Size = New System.Drawing.Size(258, 130)
        Me.TabPage3.TabIndex = 2
        Me.TabPage3.Text = "Message"
        Me.TabPage3.UseVisualStyleBackColor = True
        '
        'optGoodbye
        '
        Me.optGoodbye.AutoSize = True
        Me.optGoodbye.Location = New System.Drawing.Point(8, 40)
        Me.optGoodbye.Name = "optGoodbye"
        Me.optGoodbye.Size = New System.Drawing.Size(71, 17)
        Me.optGoodbye.TabIndex = 1
        Me.optGoodbye.TabStop = True
        Me.optGoodbye.Text = "Goodbye!"
        Me.optGoodbye.UseVisualStyleBackColor = True
        '
        'optHello
        '
        Me.optHello.AutoSize = True
        Me.optHello.Location = New System.Drawing.Point(8, 17)
        Me.optHello.Name = "optHello"
        Me.optHello.Size = New System.Drawing.Size(52, 17)
        Me.optHello.TabIndex = 0
        Me.optHello.TabStop = True
        Me.optHello.Text = "Hello!"
        Me.optHello.UseVisualStyleBackColor = True
        '
        'displayLabel
        '
        Me.displayLabel.AutoSize = True
        Me.displayLabel.Location = New System.Drawing.Point(80, 212)
        Me.displayLabel.Name = "displayLabel"
        Me.displayLabel.Size = New System.Drawing.Size(0, 13)
        Me.displayLabel.TabIndex = 2
        '
        'frmMenuTab
        '
        Me.AutoScaleDimensions = New System.Drawing.SizeF(6.0!, 13.0!)
        Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
        Me.ClientSize = New System.Drawing.Size(266, 257)
        Me.Controls.Add(Me.displayLabel)
        Me.Controls.Add(Me.TabControl1)
        Me.Controls.Add(Me.MenuStrip1)
        Me.MainMenuStrip = Me.MenuStrip1
        Me.Name = "frmMenuTab"
        Me.Text = "Menu and Tabs"
        Me.MenuStrip1.ResumeLayout(False)
        Me.MenuStrip1.PerformLayout()
        Me.TabControl1.ResumeLayout(False)
        Me.TabPage1.ResumeLayout(False)
        Me.TabPage1.PerformLayout()
        Me.TabPage2.ResumeLayout(False)
        Me.TabPage2.PerformLayout()
        Me.TabPage3.ResumeLayout(False)
        Me.TabPage3.PerformLayout()
        Me.ResumeLayout(False)
        Me.PerformLayout()

    End Sub

    Friend WithEvents MenuStrip1 As MenuStrip
    Friend WithEvents FileToolStripMenuItem As ToolStripMenuItem
    Friend WithEvents CloseToolStripMenuItem As ToolStripMenuItem
    Friend WithEvents ExitToolStripMenuItem As ToolStripMenuItem
    Friend WithEvents EditToolStripMenuItem As ToolStripMenuItem
    Friend WithEvents ColorToolStripMenuItem As ToolStripMenuItem
    Friend WithEvents SizeToolStripMenuItem As ToolStripMenuItem
    Friend WithEvents DeleteToolStripMenuItem As ToolStripMenuItem
    Friend WithEvents MessageToolStripMenuItem As ToolStripMenuItem
    Friend WithEvents HelloToolStripMenuItem As ToolStripMenuItem
    Friend WithEvents GoodbyeToolStripMenuItem As ToolStripMenuItem
    Friend WithEvents BlackToolStripMenuItem As ToolStripMenuItem
    Friend WithEvents RedToolStripMenuItem As ToolStripMenuItem
    Friend WithEvents GreenToolStripMenuItem As ToolStripMenuItem
    Friend WithEvents ToolStripMenuItem2 As ToolStripMenuItem
    Friend WithEvents ToolStripMenuItem3 As ToolStripMenuItem
    Friend WithEvents ToolStripMenuItem4 As ToolStripMenuItem
    Friend WithEvents TabControl1 As TabControl
    Friend WithEvents TabPage1 As TabPage
    Friend WithEvents TabPage2 As TabPage
    Friend WithEvents TabPage3 As TabPage
    Friend WithEvents optGreen As RadioButton
    Friend WithEvents optRed As RadioButton
    Friend WithEvents optBlack As RadioButton
    Friend WithEvents opt20 As RadioButton
    Friend WithEvents opt16 As RadioButton
    Friend WithEvents opt12 As RadioButton
    Friend WithEvents optGoodbye As RadioButton
    Friend WithEvents optHello As RadioButton
    Friend WithEvents displayLabel As Label
End Class
