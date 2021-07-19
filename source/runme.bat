@echo off
echo input text = input.txt
echo output wav = output.wav
pause
flite --setf int_f0_target_stddev=25 --setf int_f0_target_mean=115 -f input.txt -o output.wav
echo done! you can now close this window!
pause
