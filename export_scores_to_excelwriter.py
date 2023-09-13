#import pandas as pd
import sys
import xlsxwriter


def export_one_model_scores(src, trg, trans, score, outfile):
    workbook = xlsxwriter.Workbook(f'{outfile}.xlsx')
    worksheet = workbook.add_worksheet("scores")
    # text formatting
    text_format = workbook.add_format()
    text_format.set_text_wrap()
    text_format.set_align('top')
    # number formatting
    score_format = workbook.add_format()
    score_format.set_align('top')
    score_format.set_num_format('0.0000')
    # header formatting
    header_format = workbook.add_format()
    header_format.set_align('center')
    header_format.set_bold()
    row = 0
    column = 0
    headers = ['source', 'translation', 'score', 'reference']
    for header in headers:
        worksheet.write(row, column, header, header_format)
        column += 1
    # set column width: text is 40 and score is 7
    worksheet.set_column(0, 0, 40)
    worksheet.set_column(1, 1, 40)
    worksheet.set_column(2, 2, 7)
    worksheet.set_column(3, 3, 40)
    # reset counters
    column = 0
    row = 1
    # write rows to the table
    # we need to know the length of the file
    src_lines = src.readlines()
    src_len = len(src_lines)
    for sline in src_lines:
        sline = sline.strip()
        tline = trg.readline().strip()
        trline = trans.readline().strip()
        scoreline = float(score.readline().strip())
        values = [sline, trline, scoreline, tline]
        for value in values:
            if isinstance(value, float):
                worksheet.write(row, column, value, score_format)
            else:
                worksheet.write(row, column, value, text_format)
            column += 1
        column = 0
        row += 1
    # apply filter to known length
    worksheet.autofilter(0, 0, src_len, 3)
    workbook.close()


def export_two_model_scores(src, trg, trans1, score1, trans2, score2, outfile):
    workbook = xlsxwriter.Workbook(f'{outfile}.xlsx')
    worksheet = workbook.add_worksheet("scores_diff")
    # text formatting
    text_format = workbook.add_format()
    text_format.set_text_wrap()
    text_format.set_align('top')
    # number formatting
    score_format = workbook.add_format()
    score_format.set_align('top')
    score_format.set_num_format('0.0000')
    # header formatting
    header_format = workbook.add_format()
    header_format.set_align('center')
    header_format.set_bold()
    row = 0
    column = 0
    headers = ['source', 'translation1', 'score1', 'translation2', 'score2', 'reference', 'score2-score1']
    for header in headers:
        worksheet.write(row, column, header, header_format)
        column += 1
    # set column width: text is 40 and score is 7
    worksheet.set_column(0, 0, 30)
    worksheet.set_column(1, 1, 30)
    worksheet.set_column(2, 2, 7)
    worksheet.set_column(3, 3, 30)
    worksheet.set_column(4, 4, 7)
    worksheet.set_column(5, 5, 30)
    worksheet.set_column(6, 6, 7)
    # reset counters
    column = 0
    row = 1
    # write rows to the table
    # we need to know the length of the file
    src_lines = src.readlines()
    src_len = len(src_lines)
    for sline in src_lines:
        sline = sline.strip()
        tline = trg.readline().strip()
        trline1 = trans1.readline().strip()
        scoreline1 = float(score1.readline().strip())
        trline2 = trans2.readline().strip()
        scoreline2 = float(score2.readline().strip()) 
        diff = scoreline2 - scoreline1
        values = [sline, trline1, scoreline1, trline2, scoreline2, tline, diff]
        for value in values:
            if isinstance(value, float):
                worksheet.write(row, column, value, score_format)
            else:
                worksheet.write(row, column, value, text_format)
            column += 1
        column = 0
        row += 1
    # apply filter to known length
    worksheet.autofilter(0, 0, src_len, 6)
    workbook.close()
    


def main():
    src_file = open(sys.argv[1], 'r', encoding="utf-8", errors="ignore")
    trg_file = open(sys.argv[2], 'r', encoding="utf-8", errors="ignore")
    if len(sys.argv) == 6:
        # one model
        trans_file = open(sys.argv[3], 'r', encoding="utf-8", errors="ignore")
        score_file = open(sys.argv[4], 'r', encoding="utf-8", errors="ignore")
        outfile = sys.argv[5]
        export_one_model_scores(src_file, trg_file, trans_file, score_file, outfile)
    elif len(sys.argv) == 8:
        # two models
        trans_file1 = open(sys.argv[3], 'r', encoding="utf-8", errors="ignore")
        score_file1 = open(sys.argv[4], 'r', encoding="utf-8", errors="ignore")
        trans_file2 = open(sys.argv[5], 'r', encoding="utf-8", errors="ignore")
        score_file2 = open(sys.argv[6], 'r', encoding="utf-8", errors="ignore")
        outfile = sys.argv[7]
        export_two_model_scores(src_file, trg_file, trans_file1, score_file1, trans_file2, score_file2, outfile)
    else:
        print("Wrong number of arguments.")
        sys.exit(0)


if __name__ == "__main__":
    main()

