from WF_2_DB.WF_2_helper import demographics_import





def DB_push(runner_path,sample_hsn,run_date,outfile_path):
    #assembly metrics contain

    #need to open out output CSV files
    #scrape them, then format them to be pusehd to DB

    import_demo = demographics_import(runner_path)

    sample_hsn = import_demo.get_lims_demographics(sample_hsn,run_date)
    print("lims imported")
    '''
    import_demo.format_lims_df()
  
    #merge_mlst,demogrpahic DF together
    import_demo.merge_dfs()

    import_demo.format_dfs()

    import_demo.database_push(run_date)

    import_demo.database_push_genes()'''

