<Global.Microsoft.VisualBasic.CompilerServices.DesignerGenerated()> _
Partial Class frmRecord
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
        Me.btnRegistrar = New System.Windows.Forms.Button()
        Me.txtNombre = New System.Windows.Forms.TextBox()
        Me.txtEdad = New System.Windows.Forms.TextBox()
        Me.txtPeso = New System.Windows.Forms.TextBox()
        Me.txtEdadMeses = New System.Windows.Forms.TextBox()
        Me.txtTemperatura = New System.Windows.Forms.TextBox()
        Me.txtEpisodios = New System.Windows.Forms.TextBox()
        Me.txtAreas = New System.Windows.Forms.TextBox()
        Me.lblNombre = New System.Windows.Forms.Label()
        Me.lblEdad = New System.Windows.Forms.Label()
        Me.lblPeso = New System.Windows.Forms.Label()
        Me.lblEdadMeses = New System.Windows.Forms.Label()
        Me.lblTemperatura = New System.Windows.Forms.Label()
        Me.lblEpisodios = New System.Windows.Forms.Label()
        Me.lblAreas = New System.Windows.Forms.Label()
        Me.gbxSintomas = New System.Windows.Forms.GroupBox()
        Me.chkFiebre = New System.Windows.Forms.CheckBox()
        Me.chkVomitos = New System.Windows.Forms.CheckBox()
        Me.chkSangrado = New System.Windows.Forms.CheckBox()
        Me.gbxSintomas.SuspendLayout()
        Me.SuspendLayout()
        '
        'btnRegistrar
        '
        Me.btnRegistrar.Location = New System.Drawing.Point(78, 209)
        Me.btnRegistrar.Name = "btnRegistrar"
        Me.btnRegistrar.Size = New System.Drawing.Size(75, 23)
        Me.btnRegistrar.TabIndex = 0
        Me.btnRegistrar.Text = "Registrar"
        Me.btnRegistrar.UseVisualStyleBackColor = True
        '
        'txtNombre
        '
        Me.txtNombre.Location = New System.Drawing.Point(78, 59)
        Me.txtNombre.Name = "txtNombre"
        Me.txtNombre.Size = New System.Drawing.Size(100, 20)
        Me.txtNombre.TabIndex = 1
        '
        'txtEdad
        '
        Me.txtEdad.Location = New System.Drawing.Point(78, 98)
        Me.txtEdad.Name = "txtEdad"
        Me.txtEdad.Size = New System.Drawing.Size(36, 20)
        Me.txtEdad.TabIndex = 2
        '
        'txtPeso
        '
        Me.txtPeso.Location = New System.Drawing.Point(78, 142)
        Me.txtPeso.Name = "txtPeso"
        Me.txtPeso.Size = New System.Drawing.Size(36, 20)
        Me.txtPeso.TabIndex = 3
        '
        'txtEdadMeses
        '
        Me.txtEdadMeses.Location = New System.Drawing.Point(109, 266)
        Me.txtEdadMeses.Name = "txtEdadMeses"
        Me.txtEdadMeses.Size = New System.Drawing.Size(35, 20)
        Me.txtEdadMeses.TabIndex = 4
        '
        'txtTemperatura
        '
        Me.txtTemperatura.Location = New System.Drawing.Point(354, 233)
        Me.txtTemperatura.Name = "txtTemperatura"
        Me.txtTemperatura.Size = New System.Drawing.Size(49, 20)
        Me.txtTemperatura.TabIndex = 5
        Me.txtTemperatura.Visible = False
        '
        'txtEpisodios
        '
        Me.txtEpisodios.Location = New System.Drawing.Point(354, 275)
        Me.txtEpisodios.Name = "txtEpisodios"
        Me.txtEpisodios.Size = New System.Drawing.Size(49, 20)
        Me.txtEpisodios.TabIndex = 6
        Me.txtEpisodios.Visible = False
        '
        'txtAreas
        '
        Me.txtAreas.Location = New System.Drawing.Point(354, 318)
        Me.txtAreas.Name = "txtAreas"
        Me.txtAreas.Size = New System.Drawing.Size(49, 20)
        Me.txtAreas.TabIndex = 7
        Me.txtAreas.Visible = False
        '
        'lblNombre
        '
        Me.lblNombre.AutoSize = True
        Me.lblNombre.Location = New System.Drawing.Point(22, 66)
        Me.lblNombre.Name = "lblNombre"
        Me.lblNombre.Size = New System.Drawing.Size(44, 13)
        Me.lblNombre.TabIndex = 8
        Me.lblNombre.Text = "Nombre"
        '
        'lblEdad
        '
        Me.lblEdad.AutoSize = True
        Me.lblEdad.Location = New System.Drawing.Point(22, 105)
        Me.lblEdad.Name = "lblEdad"
        Me.lblEdad.Size = New System.Drawing.Size(32, 13)
        Me.lblEdad.TabIndex = 9
        Me.lblEdad.Text = "Edad"
        '
        'lblPeso
        '
        Me.lblPeso.AutoSize = True
        Me.lblPeso.Location = New System.Drawing.Point(22, 149)
        Me.lblPeso.Name = "lblPeso"
        Me.lblPeso.Size = New System.Drawing.Size(31, 13)
        Me.lblPeso.TabIndex = 10
        Me.lblPeso.Text = "Peso"
        '
        'lblEdadMeses
        '
        Me.lblEdadMeses.AutoSize = True
        Me.lblEdadMeses.Location = New System.Drawing.Point(22, 273)
        Me.lblEdadMeses.Name = "lblEdadMeses"
        Me.lblEdadMeses.Size = New System.Drawing.Size(81, 13)
        Me.lblEdadMeses.TabIndex = 11
        Me.lblEdadMeses.Text = "Edad en Meses"
        '
        'lblTemperatura
        '
        Me.lblTemperatura.AutoSize = True
        Me.lblTemperatura.Location = New System.Drawing.Point(281, 240)
        Me.lblTemperatura.Name = "lblTemperatura"
        Me.lblTemperatura.Size = New System.Drawing.Size(67, 13)
        Me.lblTemperatura.TabIndex = 12
        Me.lblTemperatura.Text = "Temperatura"
        '
        'lblEpisodios
        '
        Me.lblEpisodios.AutoSize = True
        Me.lblEpisodios.Location = New System.Drawing.Point(281, 282)
        Me.lblEpisodios.Name = "lblEpisodios"
        Me.lblEpisodios.Size = New System.Drawing.Size(52, 13)
        Me.lblEpisodios.TabIndex = 13
        Me.lblEpisodios.Text = "Episodios"
        '
        'lblAreas
        '
        Me.lblAreas.AutoSize = True
        Me.lblAreas.Location = New System.Drawing.Point(281, 325)
        Me.lblAreas.Name = "lblAreas"
        Me.lblAreas.Size = New System.Drawing.Size(34, 13)
        Me.lblAreas.TabIndex = 14
        Me.lblAreas.Text = "Areas"
        '
        'gbxSintomas
        '
        Me.gbxSintomas.Controls.Add(Me.chkSangrado)
        Me.gbxSintomas.Controls.Add(Me.chkVomitos)
        Me.gbxSintomas.Controls.Add(Me.chkFiebre)
        Me.gbxSintomas.Location = New System.Drawing.Point(203, 34)
        Me.gbxSintomas.Name = "gbxSintomas"
        Me.gbxSintomas.Size = New System.Drawing.Size(200, 160)
        Me.gbxSintomas.TabIndex = 15
        Me.gbxSintomas.TabStop = False
        Me.gbxSintomas.Text = "Sintomas"
        '
        'chkFiebre
        '
        Me.chkFiebre.AutoSize = True
        Me.chkFiebre.Location = New System.Drawing.Point(35, 37)
        Me.chkFiebre.Name = "chkFiebre"
        Me.chkFiebre.Size = New System.Drawing.Size(55, 17)
        Me.chkFiebre.TabIndex = 0
        Me.chkFiebre.Text = "Fiebre"
        Me.chkFiebre.UseVisualStyleBackColor = True
        '
        'chkVomitos
        '
        Me.chkVomitos.AutoSize = True
        Me.chkVomitos.Location = New System.Drawing.Point(35, 60)
        Me.chkVomitos.Name = "chkVomitos"
        Me.chkVomitos.Size = New System.Drawing.Size(63, 17)
        Me.chkVomitos.TabIndex = 1
        Me.chkVomitos.Text = "Vómitos"
        Me.chkVomitos.UseVisualStyleBackColor = True
        '
        'chkSangrado
        '
        Me.chkSangrado.AutoSize = True
        Me.chkSangrado.Location = New System.Drawing.Point(35, 83)
        Me.chkSangrado.Name = "chkSangrado"
        Me.chkSangrado.Size = New System.Drawing.Size(72, 17)
        Me.chkSangrado.TabIndex = 2
        Me.chkSangrado.Text = "Sangrado"
        Me.chkSangrado.UseVisualStyleBackColor = True
        '
        'frmRecord
        '
        Me.AutoScaleDimensions = New System.Drawing.SizeF(6.0!, 13.0!)
        Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
        Me.ClientSize = New System.Drawing.Size(432, 400)
        Me.Controls.Add(Me.gbxSintomas)
        Me.Controls.Add(Me.lblAreas)
        Me.Controls.Add(Me.lblEpisodios)
        Me.Controls.Add(Me.lblTemperatura)
        Me.Controls.Add(Me.lblEdadMeses)
        Me.Controls.Add(Me.lblPeso)
        Me.Controls.Add(Me.lblEdad)
        Me.Controls.Add(Me.lblNombre)
        Me.Controls.Add(Me.txtAreas)
        Me.Controls.Add(Me.txtEpisodios)
        Me.Controls.Add(Me.txtTemperatura)
        Me.Controls.Add(Me.txtEdadMeses)
        Me.Controls.Add(Me.txtPeso)
        Me.Controls.Add(Me.txtEdad)
        Me.Controls.Add(Me.txtNombre)
        Me.Controls.Add(Me.btnRegistrar)
        Me.Name = "frmRecord"
        Me.Text = "Record del Paciente"
        Me.gbxSintomas.ResumeLayout(False)
        Me.gbxSintomas.PerformLayout()
        Me.ResumeLayout(False)
        Me.PerformLayout()

    End Sub

    Friend WithEvents btnRegistrar As Button
    Friend WithEvents txtNombre As TextBox
    Friend WithEvents txtEdad As TextBox
    Friend WithEvents txtPeso As TextBox
    Friend WithEvents txtEdadMeses As TextBox
    Friend WithEvents txtTemperatura As TextBox
    Friend WithEvents txtEpisodios As TextBox
    Friend WithEvents txtAreas As TextBox
    Friend WithEvents lblNombre As Label
    Friend WithEvents lblEdad As Label
    Friend WithEvents lblPeso As Label
    Friend WithEvents lblEdadMeses As Label
    Friend WithEvents lblTemperatura As Label
    Friend WithEvents lblEpisodios As Label
    Friend WithEvents lblAreas As Label
    Friend WithEvents gbxSintomas As GroupBox
    Friend WithEvents chkSangrado As CheckBox
    Friend WithEvents chkVomitos As CheckBox
    Friend WithEvents chkFiebre As CheckBox
End Class
