# import sys
# import time
# import shutil

# yield, a função é um gerador, e o tipo de retorno correto é Generator, não None.
# from typing import Generator, Any
# def ft_tqdm(lst: range) -> Generator[Any, Any, Any]:
# def ft_tqdm(lst: range) -> None:
# 	total = len(lst)
# 	start_time = time.time()

# 	terminal_width = shutil.get_terminal_size().columns - 30
# 	bar_length = terminal_width - 10
# 	total_digits = len(str(total))

# 	for i, item in enumerate(lst):
# 		current_time = time.time()
# 		elapsed_time = current_time - start_time
		
# 		if elapsed_time == 0:
# 			speed = 0
# 			eta = 0
# 		else:
# 			speed = (i + 1) / elapsed_time
# 			eta = (total - (i + 1)) / speed if speed > 0 else 0

# 		m_elapsed, s_elapsed = divmod(elapsed_time, 60)
# 		m_eta, s_eta = divmod(eta, 60)
		
# 		elapsed_formatted = f"{int(m_elapsed):02d}:{int(s_elapsed):02d}"
# 		eta_formatted = f"{int(m_eta):02d}:{int(s_eta):02d}"

# 		percentage = ((i + 1) / total) * 100
		
# 		filled_length = int(bar_length * percentage // 100)
# 		bar = '█' * filled_length + ' ' * (bar_length - filled_length)
		
# 		count_str = f"{i + 1:>{total_digits}}/{total:d}"
# 		output_str = f"\r{int(percentage):3d}%|{bar}| {count_str} [{elapsed_formatted}<{eta_formatted}, {speed:.2f}it/s]"

# 		print(output_str, end="", flush=True)
		
# 		yield item

# 	sys.stdout.write('\n')

## No enunciado diz "Allowed functions : None", 
## e o resultado apenas da | 333/333, sem tempo ou it/s

def ft_tqdm(lst: range) -> None:
	total = len(lst)
	bar_length = 100
	total_digits = len(str(total))

	for i, item in enumerate(lst):
		percentage = ((i + 1) / total) * 100
		
		filled_length = int(bar_length * percentage // 100)
		bar = '█' * filled_length + ' ' * (bar_length - filled_length)
		
		count_str = f"{i + 1:>{total_digits}}/{total:d}"
		output_str = f"\r{int(percentage):3d}%|{bar}| {count_str}"
		print(output_str, end="", flush=True)
		
		yield item