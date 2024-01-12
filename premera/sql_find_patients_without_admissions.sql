SELECT
  p.patient_id,
  p.first_name,
  p.last_name
FROM
  patients p
  LEFT OUTER JOIN admissions a ON a.patient_id = p.patient_id
WHERE
  a.patient_id IS NULL
  
  /*
   Start by selecting a question by pressing 'Start' or 'View All Questions'.
   Use the resources and information about the database from the left panel to help.
   Press the run button to execute the query.
   Question is automatically validated every time you execute the query.
   Make your output match the expected output.


   Keybinds:
   [ctrl + enter]: Execute the SQL
   [ctrl + q]: Auto-format the SQL
   */
